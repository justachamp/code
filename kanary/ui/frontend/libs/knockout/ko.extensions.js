// accepts jQuery node and remove boolean
ko.unapplyBindings = function($node, remove) {
    // unbind events
    $node.find('*').each(function() {
        $(this).unbind();
    });
    // Remove KO subscriptions and references
    ko.cleanNode($node[0]);
    if (remove) {
        ko.removeNode($node[0]);
    }
};
