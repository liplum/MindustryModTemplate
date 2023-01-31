import sys
import os
import io
import shutil

args = sys.argv
full_name = args[1]
owner, repo = full_name.split('/')
package_name = owner.replace("-", "")
main_class_template = """package %PackageName%;
import mindustry.mod.*;

public class %MainClassName% extends Mod {
    
}
"""
readme_template = """<div align = center>

# %Repository%

![Mod Icon](icon.png)

</div>

## Modding ToDo List:

- [x] Create a new Mindustry Java mod project.
- [ ] Edit the [mod.hjson](mod.hjson) for your mod.
- [ ] Create your first content, a block, an item or anything you want.
- [ ] Put sprites and bundles into [assets](assets) directory.
- [ ] Check the Mindustry's sources with your IDE or on its [repository](https://github.com/Anuken/Mindustry).
- [ ] Make a beautiful [mod icon](icon.png) to replace the placeholder.
- [ ] Push a commit with any message containing `[release]` to generate a release draft on [GitHub](https://github.com/%Owner%/%Repository%/releases). 
"""


def transform_repo_to_class() -> str:
    with io.StringIO() as b:
        hyphen = False
        for i, c in enumerate(repo):
            c: str
            if c == '-':
                hyphen = True
            else:
                if hyphen:
                    b.write(c.upper())
                    hyphen = False
                else:
                    if i == 0:
                        b.write(c.upper())
                    else:
                        b.write(c)
        name: str = b.getvalue()
        name = name.removesuffix("Mod")
        return name


main_class_name = transform_repo_to_class() + "Mod"
main_class_qualified_name = f"{package_name}.{main_class_name}"


def replace_mod_meta():
    text = readme_template.replace(
        "%Repository%", repo
    ).replace(
        "%Owner%", owner
    ).replace(
        "%MainClassQualifiedName%", main_class_qualified_name
    )
    with open("mod.hjson", mode='w') as mod_meta:
        mod_meta.write(text)


def generate_main_class():
    os.makedirs(f"src/{package_name}", exist_ok=True)
    with open(f"src/{package_name}/{main_class_name}.java", mode='w+') as main_clz:
        content = main_class_template.replace(
            "%PackageName%", package_name
        ).replace(
            "%MainClassName%", main_class_name
        )
        main_clz.write(content)


def replace_readme():
    with open(".github/workflows/cleanup/README.md", mode='r') as readme:
        text = readme.read()
    text = text.replace("%Repository%", repo).replace("%Owner%", owner)
    with open("README.md", mode='w') as readme:
        readme.write(text)


def delete_self():
    os.remove(".github/workflows/CleanUpTemplate.yml")
    os.remove("LICENSE")
    shutil.rmtree(".github/workflows/cleanup")


def main():
    replace_mod_meta()
    generate_main_class()
    replace_readme()
    delete_self()


if __name__ == '__main__':
    main()
