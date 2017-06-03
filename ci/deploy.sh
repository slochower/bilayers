# Exit on errors
set -o errexit

# Configure git
git config --global push.default simple
git config --global user.email `git log --max-count=1 --format='%ae'`
git config --global user.name `git log --max-count=1 --format='%an'`
git checkout $TRAVIS_BRANCH
git remote set-url origin git@github.com:slochower/bilayers.git

# Decrypt and add SSH key
openssl aes-256-cbc \
  -K $encrypted_af28e4027e49_key \
  -iv $encrypted_af28e4027e49_iv \
  -in ci/deploy.key.enc \
  -out ci/deploy.key -d
eval `ssh-agent -s`
chmod 600 ci/deploy.key
ssh-add ci/deploy.key

# Commit message
MESSAGE="\
`git log --max-count=1 --format='%s'`

This build is based on
https://github.com/slochower/bilayers/commit/$TRAVIS_COMMIT.

This commit was created by the following Travis CI build and job:
https://travis-ci.org/slochower/bilayers/builds/$TRAVIS_BUILD_ID
https://travis-ci.org/slochower/bilayers/jobs/$TRAVIS_JOB_ID

[ci skip]

The full commit message that triggered this build is copied below:

$TRAVIS_COMMIT_MESSAGE
"

git status

# # Deploy the reference data to references
# echo "Deploying references branch..."
# ghp-import --push --branch=references --message="$MESSAGE" references/generated

# echo "Deploying gh-pages branch..."
# # Deploy the output to gh-pages
# ghp-import --push --branch=gh-pages --message="$MESSAGE" output
