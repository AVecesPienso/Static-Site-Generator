import re

from textnode import TextNode, TextType

#Split delimiter
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is TextType.TEXT:
            split_text = node.text.split(delimiter)
            if len(split_text) % 2 == 1:
                for i, sentence in enumerate(split_text):
                    if sentence == "":
                        continue
                    elif i % 2 == 0:
                        new_nodes.append(TextNode(sentence, TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(sentence, text_type))
            else:
                raise Exception("Invalid Markdown syntax")
        else:
            new_nodes.append(node)
    return new_nodes

#Extract images and links
def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

#Split Images and Links
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.IMAGE:
            new_nodes.append(node)
            continue
        sentence = node.text
        markdown = extract_markdown_images(sentence)
        if markdown == []:
            new_nodes.append(node)
        else:
            while markdown != []:
                full_mark = f"![{markdown[0][0]}]({markdown[0][1]})"
                mark_list = sentence.split(full_mark, maxsplit = 1)

                if mark_list[0] != "":
                    text_node = TextNode(mark_list[0], TextType.TEXT)
                    new_nodes.append(text_node)

                image_node = TextNode(markdown[0][0], TextType.IMAGE, markdown[0][1])
                new_nodes.append(image_node)
                sentence = mark_list[1]
                markdown.pop(0)

            if sentence != "":
                text_node = TextNode(sentence, TextType.TEXT)
                new_nodes.append(text_node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.LINK:
            new_nodes.append(node)
            continue
        sentence = node.text
        markdown = extract_markdown_links(sentence)
        if markdown == []:
            new_nodes.append(node)
        else:
            while markdown != []:
                full_mark = f"[{markdown[0][0]}]({markdown[0][1]})"
                mark_list = sentence.split(full_mark, maxsplit = 1)

                if mark_list[0] != "":
                    text_node = TextNode(mark_list[0], TextType.TEXT)
                    new_nodes.append(text_node)

                link_node = TextNode(markdown[0][0], TextType.LINK, markdown[0][1])
                new_nodes.append(link_node)
                sentence = mark_list[1]
                markdown.pop(0)

            if sentence != "":
                text_node = TextNode(sentence, TextType.TEXT)
                new_nodes.append(text_node)
    return new_nodes

#Text to TextNodes
def text_to_textnodes(text):
    text_node = [TextNode(text, TextType.TEXT)]
    image_nodes = split_nodes_image(text_node)
    link_nodes = split_nodes_link(image_nodes)
    code_node = split_nodes_delimiter(link_nodes, "`", TextType.CODE)
    italic_node = split_nodes_delimiter(code_node, "_", TextType.ITALIC)
    bold_node = split_nodes_delimiter(italic_node, "**", TextType.BOLD)
    second_italic_node = split_nodes_delimiter(bold_node, "*", TextType.ITALIC)
    return second_italic_node
