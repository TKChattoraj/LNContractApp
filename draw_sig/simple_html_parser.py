from bs4 import BeautifulSoup

with open("./contract.html") as fp:
    soup = BeautifulSoup(fp)

print(soup)
tag_sig = soup.find_all("signature_block_p")
print("Signature element:")
print(tag_sig)
tag_sig[0].string = "Signed!"

tag_sig_graphic = soup.new_tag("img")
tag_sig_graphic["src"]="./pix.png"
tag_sig[0].insert(1,tag_sig_graphic)
print(soup)
string_instance=str(soup)
with open("./output.html", "w") as f:
    f.write(string_instance)