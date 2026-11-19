#
# PySNMP MIB module RIELLO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/riello/RIELLO-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:39:34 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, Counter32, TimeTicks, MibIdentifier, Gauge32, Counter64, enterprises, ObjectIdentity, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "Counter32", "TimeTicks", "MibIdentifier", "Gauge32", "Counter64", "enterprises", "ObjectIdentity", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rielloMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5491))
rielloMIB.setRevisions(('2016-02-23 00:00',))
if mibBuilder.loadTexts: rielloMIB.setLastUpdated('201602230000Z')
if mibBuilder.loadTexts: rielloMIB.setOrganization('RPS S.p.A')
mibBuilder.exportSymbols("RIELLO-MIB", PYSNMP_MODULE_ID=rielloMIB, rielloMIB=rielloMIB)
