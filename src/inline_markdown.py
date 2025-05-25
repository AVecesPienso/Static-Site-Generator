from textnode import TextNode, TextType

#Split delimiter
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is TextType.TEXT:
            split_text = node.text.split(delimiter)
            if len(split_text) % 2 == 1:
                for i, sentence in enumerate(split_text):
                    if i % 2 == 0:
                        new_nodes.append(TextNode(sentence, TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(sentence, text_type))
            else:
                raise Exception("Invalid Markdown syntax")
        else:
            new_nodes.append(node)
    return new_nodes