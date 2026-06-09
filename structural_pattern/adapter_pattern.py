class Target:
    """
    The Target defines the domain-specific interface used by the client code.
    """

    def request(self) -> str:
        return "Target: The default target's behavior"


class Adaptee:
    def specific_request(self) -> str:
        return "Adaptee: (This is specific request)"


class Adapter(Target, Adaptee):
    def request(self) -> str:
        return f"Adapter: (Translated) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    """
    The client code supports all  teh classes that follows the target interface.
    """

    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just with the Target objects:")
    target = Target()

    client_code(target)
    print()

    adaptee = Adaptee()
    print("Client: The adapter class has a weird interface.See, I don't understand it")

    print(f"Adaptee: {adaptee.specific_request()[::-1]}", end="\n\n")
    print("Client , But I can work via Adapter")
    adapter = Adapter()
    client_code(adapter)
