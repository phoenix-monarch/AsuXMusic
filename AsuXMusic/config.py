from os import getenv

from dotenv import load_dotenv

load_dotenv()

admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BQBWyIl8icee9tKdymI10oN7h8eINolbFfpUkW24IeD3QNWW17DnC46nxw4lF9eZyoJqHxzc_Z2pyfGEcz4drSy21GcGMVfY0Ri7flEMPT4G_6PynuZx6ewKyh5_UBEXxkj1P__f9owjCsDSGyXAn81cbhhVkhwr07uUqVujFTBUrcK1P8oSZp-p-ogVIveUCoQ6-Ujgos-Kkthumi-k95-cTQ4hRVAJQ41jcNFR2SSWNlnobymSFKFEKEEX-jby6C9seTOy7niaGqChY5g99fVUHdoeC-PKkbe84bIsOFWtVYeJBVmrmNiJP0wACaQLFzdE6ZM17B00mlE603JbRZDZagBYGwA")

BOT_TOKEN = getenv("BOT_TOKEN", "5841568185:AAFODqetoPeeBhBsXDyRVT7KIniZDnpWOY8")
API_ID = int(getenv("API_ID", "20570663"))
API_HASH = getenv("API_HASH", "209c97b1090c80f24eaf6b0ef880d088")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "weebs_chats")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "team_wizardz")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1488316798").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1488316798").split()))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/31e9ecee16a46575267a4.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/d744707634106cf76627a.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://te.legra.ph/file/bc5556476395a0c8e109b.jpg"
)
