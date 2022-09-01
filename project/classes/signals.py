from project.classes.signal import Signal


class Signals:
    """
    Class represent instance of Signals (list of Signal instances)
    """

    def __init__(self, signals_data: list[dict]):
        self.signals = []
        for signal in signals_data:
            self.signals.append(Signal(signal))

    def __getitem__(self, item: int) -> Signal:
        for signal in self.signals:
            if signal.sig_id == item:
                return signal

    def __str__(self):
        signal_list = [str(signal.__dict__) for signal in self.signals]
        signals_str = '\n'.join(signal_list)
        return signals_str

    def __len__(self):
        return len(self.signals)

    def __contains__(self, item: Signal):
        return item in self.signals
