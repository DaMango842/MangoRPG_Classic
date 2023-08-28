from room import Room


start = Room(
    "start",
    "起始之地",
    "???",
    "",
    "norcalPlain1",
    "",
    ""
    )
norcalPlain1 = Room(
    "norcalPlain1",
    "诺卡尔平原1",
    "暂无介绍",
    "",
    "norcalPlain2",
    "",
    "start"
    )
norcalPlain2 = Room(
    "norcalPlain2",
    "诺卡尔平原2",
    "暂无介绍",
    "",
    "norcalPlain3",
    "",
    "norcalPlain1"
    )
norcalPlain3 = Room(
    "norcalPlain3",
    "诺卡尔平原3",
    "暂无介绍",
    "",
    "",
    "",
    "norcalPlain2"
)