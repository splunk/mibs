#
# PySNMP MIB module ARUBA-VENDORTYPE (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arubaos/ARUBA-VENDORTYPE
# Produced by pysmi-1.1.12 at Thu Nov 19 08:30:55 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
arubaMIBModules, = mibBuilder.importSymbols("ARUBA-MIB", "arubaMIBModules")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, Counter64, MibIdentifier, Counter32, Gauge32, IpAddress, ObjectIdentity, TimeTicks, ModuleIdentity, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "Counter64", "MibIdentifier", "Counter32", "Gauge32", "IpAddress", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Bits", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
arubaVendorTypeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1))
arubaVendorTypeMIB.setRevisions(('2012-08-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: arubaVendorTypeMIB.setRevisionsDescriptions(('The initial revision of vendortype-oid MIB.',))
if mibBuilder.loadTexts: arubaVendorTypeMIB.setLastUpdated('201208270000Z')
if mibBuilder.loadTexts: arubaVendorTypeMIB.setOrganization('Aruba Wireless Networks')
if mibBuilder.loadTexts: arubaVendorTypeMIB.setContactInfo('Postal:    1322 Crossman Avenue\n                    Sunnyvale, CA 94089\n        E-mail:     dl-support@arubanetworks.com\n        Phone:      +1 408 227 4500')
if mibBuilder.loadTexts: arubaVendorTypeMIB.setDescription('This module describes the object identifiers that are assigned to\n        various components on aruba products.')
arubaVendorTypeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1))
arubaSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1))
aSystemUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 1))
aSystemChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 2))
aSystemBackplane = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 3))
aSystemModule = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 4))
aSystemPSU = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 5))
aSystemFAN = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 6))
aSystemContainer = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 7))
aSystemPort = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 8))
aSystemSensor = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 9))
mibBuilder.exportSymbols("ARUBA-VENDORTYPE", PYSNMP_MODULE_ID=arubaVendorTypeMIB, aSystemPSU=aSystemPSU, aSystemContainer=aSystemContainer, aSystemPort=aSystemPort, arubaVendorTypeMIB=arubaVendorTypeMIB, aSystemFAN=aSystemFAN, aSystemBackplane=aSystemBackplane, aSystemSensor=aSystemSensor, aSystemUnknown=aSystemUnknown, arubaVendorTypeMIBObjects=arubaVendorTypeMIBObjects, arubaSystem=arubaSystem, aSystemChassis=aSystemChassis, aSystemModule=aSystemModule)
