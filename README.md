<div align="center">

# Mindustry Mod Template

This template utilized [MGPP gradle plugin](https://plumygame.github.io/mgpp/) to build and debug a mod.

</div>

___

It's recommended to `watch` this project, which will notify you anything updated of the template.

## How to use this template

Hit the [green button](https://github.com/liplum/mdtmodtemplate/generate) `Use this template` above, not the `fork`, and enter your repository name, always the same as a mod name.

After the GitHub actions has done the clean-up job, you can clone your repository.

There will be a generated `main class` and `mod.hjson`.

## Building through GitHub Actions

Check the "Actions" tab on your repository page. 
Select the most recent commit in the list. 

If it completed successfully, there should be a download link under the "Artifacts" section,
that could work on both Desktop and Android.

## Generating release draft
Any push whose head commit contains `[release]` in its message, a release draft will be generated on GitHub.

## Gradle DSL and Kotlin

You can select which `Gradle DSL` to use, by easily deleting `build.gradle` or `build.gradle.kts`.
If you kept both, it would use `build.gradle` as default.

If you want to make a Kotlin mod, please keep the `build.gradle.kts` and remove `build.gradle`. 

## Licence
GNU General Public License v3.0
