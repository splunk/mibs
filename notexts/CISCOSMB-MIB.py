#
# PySNMP MIB module CISCOSMB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSMB-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, iso, Integer32, enterprises, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "Integer32", "enterprises", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cisco = ModuleIdentity((1, 3, 6, 1, 4, 1, 9))
cisco.setRevisions(('2010-10-31 00:00',))
if mibBuilder.loadTexts: cisco.setLastUpdated('201010310000Z')
if mibBuilder.loadTexts: cisco.setOrganization('Cisco Systems, Inc.')
otherEnterprises = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6))
ciscosb = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1))
switch001 = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101))
rndMib = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101))
mibBuilder.exportSymbols("CISCOSMB-MIB", cisco=cisco, switch001=switch001, otherEnterprises=otherEnterprises, PYSNMP_MODULE_ID=cisco, rndMib=rndMib, ciscosb=ciscosb)
