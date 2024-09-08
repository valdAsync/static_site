def markdown_to_blocks(markdown):
    blocks = []
    for line in markdown.split("\n\n"):
        if line == "":
            continue
        blocks.append(line.strip())
    return blocks
