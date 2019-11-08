/*Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
*/

class Node {
    constructor(val, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}


class Node {
    constructor(val, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

function serialize(root) {
    function recursiveSerialize(node) {
        if (node) {
            vals.push(node.val);
            recursiveSerialize(node.left);
            recursiveSerialize(node.right);
        } else {
            vals.push(".");
        }
    }

    let vals = new Array();
    recursiveSerialize(root);
    return vals;
};

function deserialize(data) {
    function recursiveDeserialize() {
        let val = data.shift();

        if (val === '.') {
            return null;
        } else {
            let node = new Node(Number(val));
            node.left = recursiveDeserialize();
            node.right = recursiveDeserialize();
            return node;
        }
    }
    return recursiveDeserialize();
};

const node = new Node('root', new Node('left', new Node('left.left')), new Node('right'))
console.log(deserialize(serialize(node)).left.left.val)
