#
# PySNMP MIB module FIREBRICK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/firebrick/FIREBRICK-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:09:34 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, IpAddress, Bits, Integer32, ModuleIdentity, NotificationType, iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, enterprises, ObjectIdentity, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "Bits", "Integer32", "ModuleIdentity", "NotificationType", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "enterprises", "ObjectIdentity", "Unsigned32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
firebrick = ModuleIdentity((1, 3, 6, 1, 4, 1, 24693))
firebrick.setRevisions(('2020-04-06 00:00',))
if mibBuilder.loadTexts: firebrick.setLastUpdated('202004060000Z')
if mibBuilder.loadTexts: firebrick.setOrganization('Andrews & Arnold Limited')
firebrickNewStyle = MibIdentifier((1, 3, 6, 1, 4, 1, 24693, 100))
mibBuilder.exportSymbols("FIREBRICK-MIB", firebrick=firebrick, firebrickNewStyle=firebrickNewStyle, PYSNMP_MODULE_ID=firebrick)
