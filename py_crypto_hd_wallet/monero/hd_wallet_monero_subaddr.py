# Copyright (c) 2021 Emanuele Bellocchia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


# Imports
from __future__ import annotations
import json
from typing import Dict, Iterator
from bip_utils import Monero
from py_crypto_hd_wallet.bip.hd_wallet_bip_keys import HdWalletBipKeys


class HdWalletMoneroSubddressesConst:
    """ Class container for HD wallet Monero subaddresses constants. """

    # Address key for dictionary
    ADDR_DICT_KEY: str = "subaddress_{:d}"


class HdWalletMoneroSubddresses:
    """ HD wallet Monero subaddresses class. It creates subaddresses from a Monero object and store them.
    Subaddresses can be got individually, as dictionary or in JSON format.
    """

    #
    # Public methods
    #

    def __init__(self) -> None:
        """ Construct class. """
        self.m_subaddresses = []

    @staticmethod
    def FromMoneroObj(monero_obj: Monero,
                      account_idx: int,
                      subaddr_num: int,
                      subaddr_offset: int) -> HdWalletMoneroSubddresses:
        """ Create addresses from the specified Bip object.
        If the Bip object is at address index level, only one address will be computed.

        Args:
            monero_obj (Monero object): Monero object
            account_idx (int)         : Account index
            subaddr_num (int)         : Subaddress number
            subaddr_offset (int)      : Starting subaddress index

        Returns:
            HdWalletMoneroSubddresses object: HdWalletMoneroSubddresses object
        """
        addr = HdWalletMoneroSubddresses()

        if bip_obj.IsLevel(Bip44Levels.ADDRESS_INDEX):
            addr.m_addresses.append(HdWalletBipKeys.FromBipObj(bip_obj))
        else:
            for i in range(addr_num):
                bip_obj_addr = bip_obj.AddressIndex(i + addr_off)
                addr.m_addresses.append(HdWalletBipKeys.FromBipObj(bip_obj_addr))

        return addr

    def ToDict(self) -> Dict:
        """ Get addresses as a dictionary.

        Returns:
            dict: Addresses as a dictionary
        """
        addr_dict = {}

        for i, key in enumerate(self.m_addresses):
            dict_key = HdWalletMoneroSubddressesConst.ADDR_DICT_KEY.format(i + 1)
            addr_dict[dict_key] = key.ToDict()

        return addr_dict

    def ToJson(self,
               json_indent: int = 4) -> str:
        """ Get addresses as string in JSON format.

        Args:
            json_indent (int, optional): Indent for JSON format, 4 by default

        Returns:
            str: Addresses as string in JSON format
        """
        return json.dumps(self.ToDict(), indent=json_indent)

    def Count(self) -> int:
        """ Get the addresses count.

        Returns:
            int: Number of addresses
        """
        return len(self.m_addresses)

    def __getitem__(self,
                    addr_idx: int) -> HdWalletBipKeys:
        """ Get the specified address index.

        Args:
            addr_idx (int): Address index

        Returns:
            HdWalletBipKeys object: HdWalletBipKeys object
        """
        return self.m_addresses[addr_idx]

    def __iter__(self) -> Iterator[HdWalletBipKeys]:
        """ Get the iterator to the current element.

        Returns:
            Iterator object: Iterator to the current element
        """
        yield from self.m_addresses
