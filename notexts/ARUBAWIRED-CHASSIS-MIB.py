#
# PySNMP MIB module ARUBAWIRED-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arubaos/ARUBAWIRED-CHASSIS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:30:53 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
wndFeatures, = mibBuilder.importSymbols("ARUBAWIRED-NETWORKING-OID", "wndFeatures")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, Unsigned32, Gauge32, TimeTicks, NotificationType, ModuleIdentity, MibIdentifier, Integer32, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "Unsigned32", "Gauge32", "TimeTicks", "NotificationType", "ModuleIdentity", "MibIdentifier", "Integer32", "ObjectIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
arubaWiredChassisMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11))
arubaWiredChassisMIB.setRevisions(('2020-02-13 00:00', '2020-01-07 00:00',))
if mibBuilder.loadTexts: arubaWiredChassisMIB.setLastUpdated('202002130000Z')
if mibBuilder.loadTexts: arubaWiredChassisMIB.setOrganization('HPE/Aruba Networking Division')
arubaWiredPowerSupply = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 2))
arubaWiredTempSensor = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 3))
arubaWiredFanTray = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4))
arubaWiredFan = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 5))
mibBuilder.exportSymbols("ARUBAWIRED-CHASSIS-MIB", arubaWiredFan=arubaWiredFan, arubaWiredPowerSupply=arubaWiredPowerSupply, arubaWiredTempSensor=arubaWiredTempSensor, arubaWiredFanTray=arubaWiredFanTray, PYSNMP_MODULE_ID=arubaWiredChassisMIB, arubaWiredChassisMIB=arubaWiredChassisMIB)
