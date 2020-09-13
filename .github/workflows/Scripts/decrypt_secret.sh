#!/bin/sh


# 加密命令

# gpg --symmetric --cipher-algo AES256 my_secret.json


# --批处理以防止交互式命令
# --是以假定问题的回答是“是”
gpg --quiet --batch --yes --decrypt --passphrase="1314" \
--output ./$2 $1