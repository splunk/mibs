#
# PySNMP MIB module DELIBERANT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/deliberant/DELIBERANT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:30 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Integer32, TimeTicks, ObjectIdentity, Bits, enterprises, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Unsigned32, Counter32, MibIdentifier, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "TimeTicks", "ObjectIdentity", "Bits", "enterprises", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Unsigned32", "Counter32", "MibIdentifier", "IpAddress", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
deliberant = ModuleIdentity((1, 3, 6, 1, 4, 1, 32761))
deliberant.setRevisions(('2008-09-05 00:00',))
if mibBuilder.loadTexts: deliberant.setLastUpdated('200809050000Z')
if mibBuilder.loadTexts: deliberant.setOrganization('Deliberant')
dlbProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 1))
dlbAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 2))
dlbMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 3))
dlbExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 7))
mibBuilder.exportSymbols("DELIBERANT-MIB", dlbProducts=dlbProducts, dlbExperimental=dlbExperimental, deliberant=deliberant, dlbAdmin=dlbAdmin, PYSNMP_MODULE_ID=deliberant, dlbMgmt=dlbMgmt)
