#
# PySNMP MIB module DELIBERANT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/deliberant/DELIBERANT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:31 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Unsigned32, enterprises, ModuleIdentity, Bits, iso, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Counter64, ObjectIdentity, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "enterprises", "ModuleIdentity", "Bits", "iso", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Counter64", "ObjectIdentity", "Integer32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
deliberant = ModuleIdentity((1, 3, 6, 1, 4, 1, 32761))
deliberant.setRevisions(('2008-09-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: deliberant.setRevisionsDescriptions(('First revision.',))
if mibBuilder.loadTexts: deliberant.setLastUpdated('200809050000Z')
if mibBuilder.loadTexts: deliberant.setOrganization('Deliberant')
if mibBuilder.loadTexts: deliberant.setContactInfo('\n        Deliberant Customer Support\n        E-mail: support@deliberant.com')
if mibBuilder.loadTexts: deliberant.setDescription('Deliberant central configuration module.')
dlbProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 1))
dlbAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 2))
dlbMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 3))
dlbExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 7))
mibBuilder.exportSymbols("DELIBERANT-MIB", PYSNMP_MODULE_ID=deliberant, dlbProducts=dlbProducts, dlbMgmt=dlbMgmt, dlbExperimental=dlbExperimental, deliberant=deliberant, dlbAdmin=dlbAdmin)
