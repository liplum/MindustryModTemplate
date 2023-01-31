<div align="center">

# Mindustry Mod Template

#### *[MGPP](https://plumygames.github.io/mgpp/) helps you to build and debug a Java mod.*

</div>

___

It's recommended to `watch` this project, which will notify you anything updated of the template.

## How To Use This Template

Above all, please take a look at the documentation of [MGPP](https://plumygames.github.io/mgpp/).
It'll help you to build your mod, run the Mindustry and debug your mod in game!

### GitHub Automation

- Step 1: Hit the green button [Use this template](https://github.com/liplum/MindustryModTemplate/generate) above.
- Step 2: Enter your repository name, which is used to generate `mod.hjson`.
- Step 3: After GitHub Action has done the cleanup job, clone your repository.
    ```shell
    git clone https://github.com/<your-name>/<your-repo>.git
    ```

### Manually Clone

- Step 1: Clone this template.
    ```shell
    git clone https://github.com/liplum/MindustryModTemplate.git <your-mod-name>
    ```
- Step 2: Delete `.git` folder.
  ```shell
  cd <your-mod-name>
  rm -rf .git
  ```

You need [Python 3](https://www.python.org/) installed on your computer to run the cleanup script.
Otherwise, you can just delete the [cleanup.py](cleanup.py) file in the root folder.

Replace `<author>` to your name, `<your-mod-name>` to your mod name bellow, and run the command.

```shell
python cleanup.py "<author>/<your-mod-name>"
```

It will clean up your project and generate essential files.

## Building through GitHub Actions

Check the "Actions" tab on your repository page.
Select the most recent commit in the list.

If it completed successfully, there should be a download link under the "Artifacts" section,
that could work on both Desktop and Android.

## Create a Release Draft

- Step 1: Check the "Actions" tab on your repository page.
- Step 2: Find `Creat Release Draft` on the left hand.
- Step 3: Hit `Run workflow` button and run on a branch you want, mostly, it's `master`.

Then a release draft with a `.jar` file, it's your mod, will be generated on GitHub.

## Gradle DSL and Kotlin

You can select which `Gradle DSL` to use by easily deleting either `build.gradle` or `build.gradle.kts`.

If you kept both, it would use `build.gradle` as default.

If you want to make a Kotlin mod, please delete `build.gradle`.

## Licence

GNU General Public License v3.0
