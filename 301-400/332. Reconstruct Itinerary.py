# Runtime: 220 ms, faster than 5.24% of Python3 online submissions
# Memory Usage: 14 MB, less than 6.73% of Python3 online submissions


class Solution:
    def findItinerary(self, tickets: list) -> list:
        tickets.sort(key=lambda x: x[0] + x[1])
        itinerary = []
        has_tickets = 2 ** len(tickets) - 1

        def find_ticket(departure: str) -> bool:
            nonlocal has_tickets
            if has_tickets == 0:
                itinerary.append(departure)
                return True
            for ti in range(len(tickets)):
                if has_tickets & 1 << ti != 0 and tickets[ti][0] == departure:
                    has_tickets &= ~(1 << ti)
                    if find_ticket(tickets[ti][1]):
                        itinerary.append(tickets[ti][0])
                        return True
                    has_tickets |= 1 << ti
            return False

        find_ticket('JFK')
        return itinerary[::-1]
