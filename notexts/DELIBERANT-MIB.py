#
# PySNMP MIB module DELIBERANT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/deliberant/DELIBERANT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:08:04 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter64, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, MibIdentifier, IpAddress, TimeTicks, Gauge32, Unsigned32, ModuleIdentity, NotificationType, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "MibIdentifier", "IpAddress", "TimeTicks", "Gauge32", "Unsigned32", "ModuleIdentity", "NotificationType", "Bits", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
deliberant = ModuleIdentity((1, 3, 6, 1, 4, 1, 32761))
deliberant.setRevisions(('2008-09-05 00:00',))
if mibBuilder.loadTexts: deliberant.setLastUpdated('200809050000Z')
if mibBuilder.loadTexts: deliberant.setOrganization('Deliberant')
dlbProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 1))
dlbAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 2))
dlbMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 3))
dlbExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 7))
mibBuilder.exportSymbols("DELIBERANT-MIB", dlbMgmt=dlbMgmt, deliberant=deliberant, dlbAdmin=dlbAdmin, PYSNMP_MODULE_ID=deliberant, dlbExperimental=dlbExperimental, dlbProducts=dlbProducts)
