define(
    ['text!./view.html', 'storage', 'creative'],
    function(template, storage, creative) {

        var Component = function(moduleContext) {

            var self = this;
            self.template = template;
            self.panel = null;
            self.vm = new creative.Creative();

            // A reference to the player is stored globally so that
            // we can dispose existing player before initializing a new one.
            // HACK:
            // We cannot store it in the object because it is destroyed
            // when user switches displyed content using sidebar.
            // E.g Storage -> Campagns.
            if (!window.hasOwnProperty('videojs_creative_player')) {
                window.videojs_creative_player = null;
            }

            self.activate = function(params) {

                if (creative.creatives().length === 0) {
                    return storage.init();
                }

                return $.Deferred().resolve();
            };

            self.onUrlChange = function(params) {
                var currentCreative = self.vm;

                return currentCreative.load(params.id);
            };

            /* Callback for handling video ad playback.
             * Initializes and tears down VAST player.
             */
            self.animated = function() {
                // If not video or no preview given, exit immediately.
                if (self.vm.fields.type() !== 'Video' ||
                        !self.vm.is_preview_visible()) {
                    return;
                }

                // HACK:
                // VideoJS cannot dispose a video object cleanly.
                // We have to first pause the playback, then wait until it
                // really paused and finally dispose it.
                // We are proud to present a refined version of following
                // StackOverflow hack:
                // http://stackoverflow.com/questions/25493887/
                var ready_to_initialize = $.Deferred();

                if (window.videojs_creative_player === null) {
                    ready_to_initialize.resolve();
                } else {
                    window.videojs_creative_player.pause();

                    setTimeout(function wait_until_when_video_has_paused() {
                        if (window.videojs_creative_player.paused()) {
                            // Paused - ready to dispose.
                            window.videojs_creative_player.dispose();
                            window.videojs_creative_player = null;
                            ready_to_initialize.resolve();
                        } else {
                            // Still not paused - keep waiting.
                            setTimeout(wait_until_when_video_has_paused);
                        }
                    });
                }

                ready_to_initialize.then(function() {
                    // Inititalize the player with current creative's VAST tag.
                    window.videojs_creative_player = videojs('video-preview');
                    window.videojs_creative_player.ads();
                    window.videojs_creative_player.vast({
                        url: self.vm.fields.vast_url()
                    });
                });
            };

        };

        return Component;
    });
