#
# PySNMP MIB module FIREBRICK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/firebrick/FIREBRICK-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:36:30 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, MibIdentifier, TimeTicks, Counter64, Gauge32, IpAddress, ModuleIdentity, Counter32, ObjectIdentity, iso, Integer32, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "MibIdentifier", "TimeTicks", "Counter64", "Gauge32", "IpAddress", "ModuleIdentity", "Counter32", "ObjectIdentity", "iso", "Integer32", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
firebrick = ModuleIdentity((1, 3, 6, 1, 4, 1, 24693))
firebrick.setRevisions(('2020-04-06 00:00',))
if mibBuilder.loadTexts: firebrick.setLastUpdated('202004060000Z')
if mibBuilder.loadTexts: firebrick.setOrganization('Andrews & Arnold Limited')
firebrickNewStyle = MibIdentifier((1, 3, 6, 1, 4, 1, 24693, 100))
mibBuilder.exportSymbols("FIREBRICK-MIB", firebrickNewStyle=firebrickNewStyle, firebrick=firebrick, PYSNMP_MODULE_ID=firebrick)
