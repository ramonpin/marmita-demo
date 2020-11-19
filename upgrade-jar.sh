#/usr/bin/env sh
cd marmita-sdk
./gradlew --quiet build
cp build/libs/marmita-sdk.jar ../src/marmitasdk/jars/.
