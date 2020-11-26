#!/usr/bin/env bash
FEATURESTORE_REPO=${HOME}/development/feature-store
pushd "${FEATURESTORE_REPO}" >/dev/null || exit
./gradlew --quiet build

popd >/dev/null || exit
cp "${FEATURESTORE_REPO}"/sdk/build/libs/sdk-0.1.0-SNAPSHOT-all.jar src/marmitasdk/jars/.
