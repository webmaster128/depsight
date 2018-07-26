# Return true iff a depends on b,
# i.e. b is in the dependencies of a
def depends_on(a, b, dependencies):
    if not a in dependencies:
        return False

    first_levels_deps = dependencies[a]

    # first level dependency
    if b in first_levels_deps:
        return True

    for a_dep in first_levels_deps:
        if depends_on(a_dep, b, dependencies):
            return True

    return False
