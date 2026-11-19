#
# PySNMP MIB module CISCO-IETF-PPVPN-MPLS-VPN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IETF-PPVPN-MPLS-VPN-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:07 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
mplsVpnVrfConfHighRouteThreshold, mplsVpnVrfPerfCurrNumRoutes = mibBuilder.importSymbols("MPLS-VPN-MIB", "mplsVpnVrfConfHighRouteThreshold", "mplsVpnVrfPerfCurrNumRoutes")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMplsVpnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 999))
ciscoMplsVpnMIB.setRevisions(('2003-04-17 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMplsVpnMIB.setRevisionsDescriptions(('Shorten names of identifiers and change name of the mib to from\n         CISCO-MPLS-VPN-MIB to CISCO-IETF-PPVPN-MPLS-VPN-MIB.',))
if mibBuilder.loadTexts: ciscoMplsVpnMIB.setLastUpdated('200304171200Z')
if mibBuilder.loadTexts: ciscoMplsVpnMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMplsVpnMIB.setContactInfo('        Cisco Systems, Inc.\n \t Postal: Customer Service\n         \t 170 W Tasman Drive\n         \t San Jose, CA  95134\n        \t USA\n    \t Tel: +1 800 553-NETS\n \t Email: cs-snmp@cisco.com\n         \tch-mpls-mib-team@cisco.com ')
if mibBuilder.loadTexts: ciscoMplsVpnMIB.setDescription('This MIB is an extension of the MPLS-VPN-MIB.  It contains a new\n\tnotification, mplsNumVrfRouteMaxThreshCleared, which was added with \n\tMPLS-VPN-MIB-DRAFT-05.')
cMplsVpnNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 0))
cMplsVpnObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 1))
cMplsVpnConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 2))
cMplsNumVrfRouteMaxThreshCleared = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 999, 0, 1)).setObjects(("MPLS-VPN-MIB", "mplsVpnVrfPerfCurrNumRoutes"), ("MPLS-VPN-MIB", "mplsVpnVrfConfHighRouteThreshold"))
if mibBuilder.loadTexts: cMplsNumVrfRouteMaxThreshCleared.setStatus('current')
if mibBuilder.loadTexts: cMplsNumVrfRouteMaxThreshCleared.setDescription('This notification is generated only after the number of routes\n        contained by the specified VRF reaches or attempts to exceed\n        the maximum allowed value as indicated by\n        mplsVrfMaxRouteThreshold, and then falls below this value. The\n        emission of this notification informs the operator that the\n        error condition has been cleared without the operator having to\n        query the device.')
cMplsVpnCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 1))
cMplsVpnGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 2))
cMplsVpnCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 1, 1)).setObjects(("CISCO-IETF-PPVPN-MPLS-VPN-MIB", "cMplsVpnNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cMplsVpnCompliance = cMplsVpnCompliance.setStatus('current')
if mibBuilder.loadTexts: cMplsVpnCompliance.setDescription('Compliance statement for agents that support the CISCO\n  \tMPLS VPN MIB.')
cMplsVpnNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 2, 1)).setObjects(("CISCO-IETF-PPVPN-MPLS-VPN-MIB", "cMplsNumVrfRouteMaxThreshCleared"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cMplsVpnNotificationGroup = cMplsVpnNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: cMplsVpnNotificationGroup.setDescription('Objects required for CISCO MPLS VPN notifications.')
mibBuilder.exportSymbols("CISCO-IETF-PPVPN-MPLS-VPN-MIB", cMplsVpnCompliances=cMplsVpnCompliances, cMplsVpnObjects=cMplsVpnObjects, ciscoMplsVpnMIB=ciscoMplsVpnMIB, cMplsNumVrfRouteMaxThreshCleared=cMplsNumVrfRouteMaxThreshCleared, cMplsVpnNotificationGroup=cMplsVpnNotificationGroup, cMplsVpnConform=cMplsVpnConform, cMplsVpnNotifs=cMplsVpnNotifs, cMplsVpnCompliance=cMplsVpnCompliance, PYSNMP_MODULE_ID=ciscoMplsVpnMIB, cMplsVpnGroups=cMplsVpnGroups)
