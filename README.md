# hue-volatility

## Purpose

Prior to starting this project I had never used an external Python library or API. I've started this in order to build my Python skills and gain my first experience working with data from the internet and from my network locally in one project. To achieve this, I've decided to use a library for stock market data and for [Philips Hue](https://www.philips-hue.com/). Another factor for picking the two was that I find them interesting, and wanted to work with them.

## Usage

Run `main.py` with the Bridge IP included and `b.connect()` un-commented. This only needs to be done once. The Bridge IP must stay included.

The user can edit `main.py` with the lights of their choice selected in `lights` list, and set the stock of their choice using the Ticker.

## Project Future

Currently (September 2023), the only project function is updating the colour of the lights based on real time increases and decreases in price. I'm planning to build on this by:

<ul>
  <li>Building a basic UI for the existing program</li>
  <li>Building another version of the program that is intended to run for extended periods of time, flashing when sharp (user defined) increases or decreases in price occur</li>
</ul>
