# Mindustry Mod Template
A template for Mindustry modding.

![DST](icon.png)

## Functions
- **Auto-release:** Every commit started with "\[AR]" will automatically generate a new release after succeeding in Build Task by GitHub Actions, for [Anuken/MindustryMods](https://github.com/Anuken/MindustryMods) checking. The latest auto-release will replace the old one.
- **Build Test:** To support Continuous Integration(CI), every commit will be checked for validity by building the project.
- **Easy Debug:** Running a custom gradle task "debugJar" will copy the generated mod's Jar file into Mindustry's mods folder and start game automatically. Recommend you to turn off the setting, Game>>Disable Mods On Startup Crash, in game to gain more convenience. You can configure the path of which game you want to start in gradle.properties.
- **Android Deployment Fix:** It was fixed that the task "deploy" cannot find d8 in your environment variable PATH on some platforms. Note: You still have to download Android SDK and add it into PATH.
- **Kotlin Support:** If you want to use Kotlin in your project, set the variable "useKotlin" as true in build.gradle. Build scripts will deal with the problem of duplicate files for you.