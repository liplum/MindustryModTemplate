import io.github.liplum.mindustry.*

plugins {
    kotlin("jvm") version "1.7.0"
    id("io.github.liplum.mgpp") version "1.1.10"
}

sourceSets {
    main {
        java.srcDirs("src")
    }
    test {
        java.srcDir("test")
    }
}
group= "org.example"
version= "1.0"
java {
    sourceCompatibility = JavaVersion.VERSION_1_8
    targetCompatibility = JavaVersion.VERSION_1_8
}
repositories {
    mavenCentral()
    mindustryRepo()
}
dependencies {
    importMindustry()
}
mindustry {
    dependency {
        mindustry on "v136"
        arc on "v136.1"
    }
    client {
        mindustry official "v136.1"
    }
    server {
        mindustry official "v136.1"
    }
    deploy {
        baseName = project.name
    }
}
mindustryAssets {
    root at "$projectDir/assets"
}