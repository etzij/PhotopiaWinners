
import requests



adressen = ["0x747d660c18c355f6e659afd733375c80016eeb24",
            "0xe36a0f3b5b0f13e5ba8453748f16bb2e6be5e195",
            "0x5eda3035025fcb8c8b01407b6f2e731561609b08",
            "0x7b19b72c07eec186b1ef20c9aa0a06c47a777271",
            "0xacd782b6a4d9ebfc76f5523a87715b19a2d5d4b6",
            "0xd62c172df49d17594691618c6f8d73c41210329a",
            "0x44a9affcd75ebe4d6772ab416bcdf746a5201807",
            "0x7ee10fc321f98aae526e3c9f2b7682517e3d3d64",
            "0xcc7abc949bdf6e3e603a282ae9a64e8b43a96c4a",
            "0x0b492b241ece8e17de0471903c254ceb4c5f893f",
            "0x170af212bcd8c5341bbbf287ea557b0ac9611cbc",
            "0x39f45cfbfb7340d095318d4ede9583d83158e9dc",
            "0x3936ae29e90ca1cff4edf29bcd16cca09d7c08df",
            "0x15dc00582e988ad3253102f78880aaa3e29448a5",
            "0x11d79ce73bce4c3a6928bb79720d0d70f6d1436f",
            "0x0b004e3d468228f36f3e756d96c9894240e13349",
            "0x0e2c6ef85d0e8ec4b760e59b79d7180a58a18c0f",
            "0xa86eff1737f3f90616b5499728a5ba8bf84e2220",
            "0x2662c3eae22d15e4e740339f3577bb0c3e1820cb",
            "0x86fdd6b6a0734e9075ead96ed01fe41f557e9330",
            "0x13075e264b96173be15846381d7c6b37a72c712a",
            "0x43ef0bf345ebe8b5b1584dc016dcc029569768de",
            "0xbefee83b0547c44749003ef42ea753c5a4eabfd7",
            "0x6007312a74ef37f37b2390a519325df15cc917da",
            "0xfc8921449c895d959d7c187cd990dc712455c7d1",
            "0x14adbd90732eb4fa7201ba114fb3100d8a9d093e",
            "0x6963252192cd67f2257307f0b1c0682a01861cc9",
            "0xee5dc999987def9175e005621defca2467251498",
            "0x4a34211a0bbbd9ca0326f31acbf2751271937223",
            "0x408130934adce05d82d8dc3706e29d02d91cf886",
            "0x47daf1530cc25acb4e6227ac3a98a62bfdeea086",
            "0x8578cf449ba155f26403781211654f8014828e2f",
            "0xe9ce2310054ce426cbcb9f3078afcfc7fc2f54f2",
            "0x3a8212a77b80669a0bd8d51e15db235ba53d42d8",
            "0x750b5cd849367ecbe48627e0007147cce285c84f",
            "0x88646ca8b574df1b75d832ddedfb91a9ebf5f549",
            "0xbd74eb13e9e64dc454ac3c0d614e19876a7426a6",
            "0x5221d12f146427b9a06638bd665f2a2fbc8f87ef",
            "0x4bde9f2fab6d26810d3058f0275604e9312846df",
            "0x06b844cb02a880166c7398cb92bdde1e1e420c37",
            "0xef7ba2da83231aa8610ea4d75d239a58ab27a02e",
            "0xb585481a0221136aa5d72dd8822d1db86c995f43",
            "0xca0b7278c108a1a10ee5f522235c37a9bbd91c69",
            "0x04290604d372b8dfb32495fb61f38eba137ca9bf",
            "0xb5a5f243b3830e64f1d5c9eb1028664f881931f4",
            "0xd35ea0c3481a0983843b2fb57147f4c8ce0a1847",
            "0x0c5b6ed6ea47d07b48f356f762f807f59f4cfd27",
            "0x112e3cd38b4218961fd019811e00fde9e37d3e90",
            "0x7b6698efa048b0203a44054c33803f62fe9a44f2",
            "0x4692039763e8a8fd9f085b517bb53d05477dd22f",
            "0x40698125e31da33d84666b1858fdec91ba508722",
            "0xab2da7a8d2d141ad1e1b190029246eb480b47d40",
            "0xf622ae5609c2a0125407e9c9f3b79ce695313ff4",
            "0x1afa21bef41b61b198b1782d4f806e163c8f291d",
            "0x3ce1af89b85b6eb4b8f5fa1e2face86877b5b6d1",
            "0x44234e2e47c57cf88a7c9e301c0f00c1a7781052",
            "0xcfa1664c628f75c4f58f6f4a1eba1bcc0f110c4b",
            "0xa4c90cedf9426c3f9895ade234c28c454aecb382",
            "0x9abcd812bffc1ef2e81a2dde75b5ed8809289d9d",
            "0x8581acdcaf078db5c08de91278ffc06c9a8a003d",
            "0x2cbf724b36bb47a3f992fad8000f6eb1e5a01932",
            "0x4d2420a4d983fdeb453daf3c8ec4306d219d1834",
            "0x20e89aa0ef531121443142734d64bad6f485f3d9",
            "0xea02975ac761a8fe34d3a8b29ecdaa7cbf766c61",
            "0xa7e40b2aa3496ad3447217d9aff26514a7bc829e",
            "0x23e95f1cfdc7ced25bca3f69907369e3097716e1",
            "0x2bc8a7aa62f70d5b0fcec2c02117ec9d49f590be",
            "0x422b59b27742885dc687c4bfef9a2e15051b0b37",
            "0x637b87dbd609bef12f8d164d306c0ce7dae65057",
            "0x3c7f5d75442b7f0322ae03472c81f231dfb05f8b",
            "0xa0a32ea25a9583f25b1152b2b24d39b0b9867302",
            "0xb792aa01d8526fb630f7d763bcb34a239a0229d4",
            "0xdeab3f7094a77199ae670316976654c17fea35d6",
            "0x4a6da59dc4aa1a209850f63b637abe6f7bd8947e",
            "0xedd27d1a5390e7b7914c3aefb729ef77bed2275b",
            "0x57859ab96be6e533c7492e4831bd2f5c1a4aaee4",
            "0xecf0217ffcf4c269c48c2515c169363d50cb19a5",
            "0x54ea5e8744f8aeb25d254a7027ec5bb0b8577a92",
            "0x872eb3673f6b7bf4d207d28640baacc60cb000b3",
            "0xe1dec865a0e80f3f437fb86342e6e922f2d603c4",
            "0xf466bdf238717ea24272d4412d170acb1712725a",
            "0xf7e688adea071a9fc766300a9b08fb1d9c522589",
            "0x980e22587fc29d25cf2c82baa6933dc0f73c09c4",
            "0xf4888bef1f0d52157b6daf7b441b5733c3a93f20",

            ]


#Titel um Metadata der einzelnen NFT zu unterscheiden
titels = ["Gundicha Temple", "Burning Man", "Far Away", "Night falls on Manhattan", "In the Woods", "Kiev-Vydybichi", "X-Ray Car", "With or without you", "Raila", "Walking the Universe", "Enter", "Kamasi Washington", "Freckled Light", "Hamburg Trichromatic", "Frau in der Pariser Metro", "Baden-Festival-Sammlung 01 Cassio Vasconcellos"]


#url um über die ABI von alchemy die Metadata der NFT zu den dazugehören adressen aufzurufen
#bei YOURALCHEMYKEY den bereitsgestellten secret abi key von alchemy eintragen
url = "https://eth-mainnet.g.alchemy.com/nft/v2/YOURALCHEMYKEY/getNFTs?owner=0x747d660c18c355f6e659afd733375c80016eeb24&contractAddresses%5B%5D=0xAf555c317608d4F9AebAe2C97bB2984656F408DF&withMetadata=true"


headers = {"accept": "application/json"}

#Liste um die Gewinner, also die alle 16 verschiedenen Bilder besitzten festzuhalten
winners = []


#iteration über die einzelnen Teilnehmeradressen um die jeweiligen Metadata herauszufinden -> URL wird jeweils angepasst
for i in adressen:
    url = "https://eth-mainnet.g.alchemy.com/nft/v2/YOURALCHEMYKEY/getNFTs?owner=" + i + "&contractAddresses%5B%5D=0xAf555c317608d4F9AebAe2C97bB2984656F408DF&withMetadata=true"
    counter = 0
    #iteration über die einzelnen titel um herauszufinden ob jeder der Titel bei der spezifischen adresse vorhanden ist
    for j in titels:
        response = requests.get(url, headers=headers)
        if j in response.text:
            counter += 1
            if counter >= 16:
                print(i)
            winners.append(i)
        else:
            break


#Ausgabe der Gewinner und der Anzahl der Gewinner
print(winners)
print(len(winners))





