import org.gradle.api.internal.tasks.testing.DecoratingTestDescriptor
import org.gradle.api.internal.tasks.testing.results.DefaultTestResult

plugins {
    scala
    application
}

repositories {
    jcenter()
}

dependencies {
    implementation("org.scala-lang:scala-library:2.13.3")
    testImplementation("junit:junit:4.12")
}

application {
    getMainClass().set("repo.sdk.App")
}

tasks {
    test {
        testLogging {
            showExceptions = true
            afterTest(KotlinClosure2<DecoratingTestDescriptor, DefaultTestResult, Unit>({ desc, result ->
                logger.quiet("  - ${desc.className}.${desc.name} with result: ${result.resultType}")
            }))
        }
    }
}
