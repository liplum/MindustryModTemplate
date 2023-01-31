import io.github.liplum.mindustry.*

plugins {
    kotlin("jvm") version "1.8.0"
    id("io.github.liplum.mgpp") version "1.2.0"
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
        mindustry mirror "v141.2"
        arc on "v141.3"
    }
    client {
        mindustry official "v141.3"
    }
    server {
        mindustry official "v141.3"
    }
    deploy {
        baseName = project.name
    }
}
mindustryAssets {
    root at "$projectDir/assets"
}