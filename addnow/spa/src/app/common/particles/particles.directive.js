(function() {
  'use strict';

  /* global particlesJS */

  function particles() {
    return {
      restrict: 'A',
      replace: true,
      transclude: true,
      template: '<div class="particleJs" id="particleJs" ng-transclude></div>',
      link: function() {
        // jscs:disable requireCamelCaseOrUpperCaseIdentifiers
        particlesJS('particleJs', {
          particles: {
            number: {
              value: 60,
              density: {
                enable: true,
                value_area: 480
              }
            },
            color: {
              value: '#e2e2e2'
            },
            shape: {
              type: 'circle',
              stroke: {
                width: 0,
                color: '#e2e2e2'
              }
            },
            opacity: {
              value: 1,
              random: false,
              anim: {
                enable: false,
                speed: 1,
                opacity_min: 0.1,
                sync: false
              }
            },
            size: {
              value: 46,
              random: true,
              anim: {
                enable: false,
                speed: 40,
                size_min: 0.1,
                sync: false
              }
            },
            line_linked: {
              enable: true,
              distance: 150,
              color: '#e2e2e2',
              opacity: 1,
              width: 1
            },
            move: {
              enable: true,
              speed: 6,
              direction: 'none',
              random: false,
              straight: false,
              out_mode: 'out',
              attract: {
                enable: false,
                rotateX: 600,
                rotateY: 1200
              }
            }
          },
          interactivity: {
            detect_on: 'canvas',
            events: {
              onhover: {
                enable: true,
                mode: 'grab'
              },
              onclick: {
                enable: true,
                mode: 'push'
              },
              resize: true
            },
            modes: {
              grab: {
                distance: 400,
                line_linked: {
                  opacity: 1
                }
              },
              bubble: {
                distance: 400,
                size: 40,
                duration: 2,
                opacity: 8,
                speed: 3
              },
              repulse: {
                distance: 200
              },
              push: {
                particles_nb: 4
              },
              remove: {
                particles_nb: 2
              }
            }
          },
          retina_detect: true,
          config_demo: {
            hide_card: false,
            background_color: '#b61924',
            background_image: '',
            background_position: '50% 50%',
            background_repeat: 'no-repeat',
            background_size: 'cover'
          }
        });

        // jscs:enable requireCamelCaseOrUpperCaseIdentifiers
      }
    };
  }

  angular.module('angulardash.common').directive('particles', particles);

})();
