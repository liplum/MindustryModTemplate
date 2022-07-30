<div align="center">

# Mindustry Mod Template

This template utilized [MGPP gradle plugin](https://plumygame.github.io/mgpp/) to build and debug a mod.

</div>

___

It's recommended to `watch` this project, which will notify you anything updated of the template.


## Building through GitHub Actions
Check the "Actions" tab on your repository page. 
Select the most recent commit in the list. 
If it completed successfully, there should be a download link under the "Artifacts" section,
that could work on both Desktop and Android.

## Generating release draft
Any push whose head commit contains `[release]` in its message, a release draft will be generated on GitHub.

## Gradle DSL

You can select which `Gradle DSL` to use, by easily deleting `build.gradle` or `build.gradle.kts`.
If you kept both, it would use `build.gradle` as default.

## Licence
GNU General Public License v3.0