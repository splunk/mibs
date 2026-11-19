#
# PySNMP MIB module ARUBAWIRED-MGMD-RMON-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arubaos/ARUBAWIRED-MGMD-RMON-TRAP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:30:55 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
wndFeatures, = mibBuilder.importSymbols("ARUBAWIRED-NETWORKING-OID", "wndFeatures")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
eventIndex, eventDescription = mibBuilder.importSymbols("RMON-MIB", "eventIndex", "eventDescription")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, Counter64, MibIdentifier, Counter32, Gauge32, IpAddress, ObjectIdentity, TimeTicks, ModuleIdentity, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "Counter64", "MibIdentifier", "Counter32", "Gauge32", "IpAddress", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Bits", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
arubaWiredMgmdRmonTrapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 4))
arubaWiredMgmdRmonTrapMIB.setRevisions(('2017-11-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: arubaWiredMgmdRmonTrapMIB.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: arubaWiredMgmdRmonTrapMIB.setLastUpdated('201711020000Z')
if mibBuilder.loadTexts: arubaWiredMgmdRmonTrapMIB.setOrganization('HPE/Aruba Networking Division')
if mibBuilder.loadTexts: arubaWiredMgmdRmonTrapMIB.setContactInfo('Hewlett Packard Company\r\n                       8000 Foothills Blvd.\r\n                       Roseville, CA 95747')
if mibBuilder.loadTexts: arubaWiredMgmdRmonTrapMIB.setDescription('This MIB module describes objects to configure\r\n               RMON traps.')
arubaWiredMgmdRmonTrapNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 4, 1))
arubaWiredMgmdRmonTrapEvent = NotificationType((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 4, 1, 1)).setObjects(("RMON-MIB", "eventIndex"), ("RMON-MIB", "eventDescription"))
if mibBuilder.loadTexts: arubaWiredMgmdRmonTrapEvent.setStatus('current')
if mibBuilder.loadTexts: arubaWiredMgmdRmonTrapEvent.setDescription('The event ID for which the trap is set has occured.')
mibBuilder.exportSymbols("ARUBAWIRED-MGMD-RMON-TRAP-MIB", arubaWiredMgmdRmonTrapNotifications=arubaWiredMgmdRmonTrapNotifications, arubaWiredMgmdRmonTrapMIB=arubaWiredMgmdRmonTrapMIB, PYSNMP_MODULE_ID=arubaWiredMgmdRmonTrapMIB, arubaWiredMgmdRmonTrapEvent=arubaWiredMgmdRmonTrapEvent)
