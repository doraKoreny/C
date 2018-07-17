def scrolling_text(text):
    scrolledtext = [text.upper()]
    for i in range(len(text)-1):
        text = text[1:] + text[0]
        scrolledtext.append(text.upper())
    print(scrolledtext)


scrolling_text("abc")
