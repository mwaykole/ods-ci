from kfp import compiler, dsl

common_base_image = (
    "registry.redhat.io/ubi9/python-312@sha256:e80ff3673c95b91f0dafdbe97afb261eab8244d7fd8b47e20ffcbcfee27fb168"
)


@dsl.component(base_image=common_base_image)
def print_message(message: str):
    """Prints a message"""
    print(message + " (step 1)")


@dsl.pipeline(name="version-test-pipeline", description="Pipeline that prints a hello message")
def version_test_pipeline(message: str = "Hello world"):
    print_message(message=message).set_caching_options(False)


if __name__ == "__main__":
    compiler.Compiler().compile(version_test_pipeline, package_path=__file__.replace(".py", "_compiled.yaml"))
