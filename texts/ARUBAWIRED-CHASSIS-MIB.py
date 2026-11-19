#
# PySNMP MIB module ARUBAWIRED-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arubaos/ARUBAWIRED-CHASSIS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:30:55 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
wndFeatures, = mibBuilder.importSymbols("ARUBAWIRED-NETWORKING-OID", "wndFeatures")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, Counter64, MibIdentifier, Counter32, Gauge32, IpAddress, ObjectIdentity, TimeTicks, ModuleIdentity, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "Counter64", "MibIdentifier", "Counter32", "Gauge32", "IpAddress", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Bits", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
arubaWiredChassisMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11))
arubaWiredChassisMIB.setRevisions(('2020-02-13 00:00', '2020-01-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: arubaWiredChassisMIB.setRevisionsDescriptions(('Added temperature sensor, fan tray, and fan entries.', 'Initial revision.',))
if mibBuilder.loadTexts: arubaWiredChassisMIB.setLastUpdated('202002130000Z')
if mibBuilder.loadTexts: arubaWiredChassisMIB.setOrganization('HPE/Aruba Networking Division')
if mibBuilder.loadTexts: arubaWiredChassisMIB.setContactInfo('Hewlett Packard Company\r\n                  8000 Foothills Blvd.\r\n                  Roseville, CA 95747')
if mibBuilder.loadTexts: arubaWiredChassisMIB.setDescription('This MIB module describes management objects that manage Chassis\r\n         components.')
arubaWiredPowerSupply = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 2))
arubaWiredTempSensor = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 3))
arubaWiredFanTray = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4))
arubaWiredFan = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 5))
mibBuilder.exportSymbols("ARUBAWIRED-CHASSIS-MIB", arubaWiredChassisMIB=arubaWiredChassisMIB, arubaWiredFan=arubaWiredFan, arubaWiredTempSensor=arubaWiredTempSensor, PYSNMP_MODULE_ID=arubaWiredChassisMIB, arubaWiredFanTray=arubaWiredFanTray, arubaWiredPowerSupply=arubaWiredPowerSupply)
