#!/usr/bin/env python3
"""Discover a small exact branch-bag template cover for four bouquets."""

from itertools import product

from reserved_terminal_specific_web_quotient_verify import minor_model
from near_k7_four_bouquet_verify import LABELS, edges_for, render, verify


def works(model, profile):
    try:
        verify(model, edges_for(profile))
    except AssertionError:
        return False
    return True


def main():
    uncovered = set(product(LABELS, repeat=4))
    templates = []
    while uncovered:
        seed = min(uncovered)
        model = minor_model(13, edges_for(seed), 7)
        assert model is not None, seed
        cover = {profile for profile in uncovered if works(model, profile)}
        assert seed in cover
        templates.append((seed, model, len(cover)))
        uncovered -= cover
        print(len(templates), "seed", seed, "covers", len(cover),
              "remaining", len(uncovered), render(model))
    print("templates", len(templates))


if __name__ == "__main__":
    main()
