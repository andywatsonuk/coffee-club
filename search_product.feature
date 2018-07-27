Feature: Search the Internet
Scenario: Search for the missing droids
	Given I launch browser on desktop PC
	When I search for the droids
	Then Relevant search results should be shown