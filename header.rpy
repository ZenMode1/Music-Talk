init -990 python in mas_submod_utils:

    Submod(
        author="zenmode",
        name="Music Talk",
        description=_("A simple dialogue add-on in which Monika analyzes song lyrics with you! It also adds some other bonus dialogue, but the focus here is music~"),
        version="0.0.6",
    )


init -989 python:

    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Music Talk",
            user_name="zenmode",
            repository_name="Music-Talk",
            extraction_depth=3
        )
