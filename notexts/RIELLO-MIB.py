#
# PySNMP MIB module RIELLO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/riello/RIELLO-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:14:16 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Unsigned32, enterprises, Integer32, Bits, iso, ModuleIdentity, Counter32, Gauge32, TimeTicks, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Unsigned32", "enterprises", "Integer32", "Bits", "iso", "ModuleIdentity", "Counter32", "Gauge32", "TimeTicks", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rielloMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5491))
rielloMIB.setRevisions(('2016-02-23 00:00',))
if mibBuilder.loadTexts: rielloMIB.setLastUpdated('201602230000Z')
if mibBuilder.loadTexts: rielloMIB.setOrganization('RPS S.p.A')
mibBuilder.exportSymbols("RIELLO-MIB", rielloMIB=rielloMIB, PYSNMP_MODULE_ID=rielloMIB)
