# Netdiff Sample Challenge

<p style="text-align: center;"><img width="800px" src='https://user-images.githubusercontent.com/56113566/230959659-aeef87d1-0b41-4b80-8851-7e412579c75a.gif'></p>

![-------------------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

This is a sample challenge based on the [netdiff library](https://github.com/openwisp/netdiff).

## Problem Statement 📜

### Adding a `ZeroTierParser` to the [`netdiff.parser`](https://github.com/openwisp/netdiff/tree/master/netdiff/parsers)

The task is to add a `ZeroTierParser` to the [netdiff.parser module](https://github.com/openwisp/netdiff/tree/master/netdiff/parsers) The parser should be able to accept ZeroTier peer information from either our sample [zerotier-peers.json](./zerotier-peers.json) file, using the `zerotier-cli peers -j` command, or the [ZeroTierServiceAPI](https://docs.zerotier.com/service/v1/#operation/getPeers).

The following points should be kept in mind while completing the task:

- Ensure that all peer information is considered while implementing the parser.

- The role and latency fields can be used for setting the cost of links.

- The `ZeroTierParser` should return a [networkx.Graph](https://networkx.org/) object.

- Additionally, The `ZeroTierParser` should also have a json method that can return valid [NetJSON output](https://github.com/openwisp/netdiff#netjson-output). This json output should be similar to the [result.json](./result.json) file provided in the repository.
## Possible Solution 👨‍💻

Here's how we can implement the [`ZeroTierParser`](./solution/netdiff/parsers/zerotier.py):

- To create the [ZeroTierParser](./solution/netdiff/parsers/zerotier.py), we can extend the netdiff [BaseParser](https://github.com/openwisp/netdiff/blob/master/netdiff/parsers/base.py).

- Currently, the parsing logic is simple. For every ZeroTier peer with any role, a node is added to the graph instance along with other ZeroTier peer properties.

- For every valid ZeroTier peer, we can collect all possible paths and parse them to add graph edges.

- To determine the cost of the graph edge, we can use the peer latency.

- It's important to note that this approach may vary, but it should still fulfill the [above-mentioned requirements](https://github.com/Aryamanz29/netdiff-task#problem-statement-).

## Output 📸

- Before proceeding, ensure that you add the code present in the [solution](./solution/) directory to the [netdiff library](https://github.com/openwisp/netdiff/tree/master/netdiff).

  ![result](https://user-images.githubusercontent.com/56113566/230972439-9fb6da1b-f2a0-4e7b-ba64-ff772eaae643.png)

## References 🔗

- ZeroTier https://docs.zerotier.com
- Netdiff https://github.com/openwisp/netdiff
- Networkx https://networkx.org/
- NetJSON https://netjson.org/docs/index.html

![-------------------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)