#
# PySNMP MIB module ARUBAWIRED-MGMD-RMON-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arubaos/ARUBAWIRED-MGMD-RMON-TRAP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:30:53 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
wndFeatures, = mibBuilder.importSymbols("ARUBAWIRED-NETWORKING-OID", "wndFeatures")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
eventIndex, eventDescription = mibBuilder.importSymbols("RMON-MIB", "eventIndex", "eventDescription")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, Unsigned32, Gauge32, TimeTicks, NotificationType, ModuleIdentity, MibIdentifier, Integer32, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "Unsigned32", "Gauge32", "TimeTicks", "NotificationType", "ModuleIdentity", "MibIdentifier", "Integer32", "ObjectIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
arubaWiredMgmdRmonTrapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 4))
arubaWiredMgmdRmonTrapMIB.setRevisions(('2017-11-02 00:00',))
if mibBuilder.loadTexts: arubaWiredMgmdRmonTrapMIB.setLastUpdated('201711020000Z')
if mibBuilder.loadTexts: arubaWiredMgmdRmonTrapMIB.setOrganization('HPE/Aruba Networking Division')
arubaWiredMgmdRmonTrapNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 4, 1))
arubaWiredMgmdRmonTrapEvent = NotificationType((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 4, 1, 1)).setObjects(("RMON-MIB", "eventIndex"), ("RMON-MIB", "eventDescription"))
if mibBuilder.loadTexts: arubaWiredMgmdRmonTrapEvent.setStatus('current')
mibBuilder.exportSymbols("ARUBAWIRED-MGMD-RMON-TRAP-MIB", arubaWiredMgmdRmonTrapMIB=arubaWiredMgmdRmonTrapMIB, arubaWiredMgmdRmonTrapEvent=arubaWiredMgmdRmonTrapEvent, arubaWiredMgmdRmonTrapNotifications=arubaWiredMgmdRmonTrapNotifications, PYSNMP_MODULE_ID=arubaWiredMgmdRmonTrapMIB)
