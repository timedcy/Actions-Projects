#!/bin/sh

# --批处理以防止交互式命令
# --是以假定问题的回答是“是”
gpg --quiet --batch --yes --decrypt --passphrase="$LARGE_SECRET_PASSPHRASE" \
--output ./my_secret.sh $1