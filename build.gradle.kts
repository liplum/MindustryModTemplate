import io.github.liplum.mindustry.*

plugins {
    kotlin("jvm") version "1.9.21"
    id("io.github.liplum.mgpp") version "1.3.0"
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
tasks.withType<KotlinCompile> {
    kotlinOptions.jvmTarget = "1.8"
}
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
        mindustry on "v146"
        arc on "v146"
    }
    client {
        mindustry official "v146"
    }
    server {
        mindustry official "v146"
    }
    deploy {
        baseName = project.name
    }
}
mindustryAssets {
    root at "$projectDir/assets"
}