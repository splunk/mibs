#
# PySNMP MIB module DELIBERANT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/deliberant/DELIBERANT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:08:05 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, MibIdentifier, Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Bits, Unsigned32, ModuleIdentity, TimeTicks, Counter32, ObjectIdentity, IpAddress, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Bits", "Unsigned32", "ModuleIdentity", "TimeTicks", "Counter32", "ObjectIdentity", "IpAddress", "NotificationType", "iso")
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
mibBuilder.exportSymbols("DELIBERANT-MIB", dlbMgmt=dlbMgmt, dlbExperimental=dlbExperimental, PYSNMP_MODULE_ID=deliberant, dlbAdmin=dlbAdmin, dlbProducts=dlbProducts, deliberant=deliberant)
