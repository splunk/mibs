#
# PySNMP MIB module GARDEROS-PRODUCT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/garderos/GARDEROS-PRODUCT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:36:40 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
garderos, = mibBuilder.importSymbols("GARDEROS-SMI-MIB", "garderos")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, NotificationType, ModuleIdentity, Counter64, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, iso, MibIdentifier, ObjectIdentity, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "ModuleIdentity", "Counter64", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "iso", "MibIdentifier", "ObjectIdentity", "Gauge32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
product = ModuleIdentity((1, 3, 6, 1, 4, 1, 16108, 1))
product.setRevisions(('2017-03-06 13:59',))
if mibBuilder.loadTexts: product.setLastUpdated('201703061359Z')
if mibBuilder.loadTexts: product.setOrganization('Garderos GmbH')
productMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 1))
if mibBuilder.loadTexts: productMIB.setStatus('current')
productConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 1, 2))
if mibBuilder.loadTexts: productConformance.setStatus('current')
productGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 1, 2, 1))
if mibBuilder.loadTexts: productGroups.setStatus('current')
productCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 1, 2, 2))
if mibBuilder.loadTexts: productCompliances.setStatus('current')
productModuleCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 16108, 1, 1, 2, 2, 1)).setObjects(("GARDEROS-PRODUCT-MIB", "productInformationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    productModuleCompliance = productModuleCompliance.setStatus('current')
productInformationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 16108, 1, 1, 2, 1, 2)).setObjects(("GARDEROS-PRODUCT-MIB", "productType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    productInformationGroup = productInformationGroup.setStatus('current')
productCasingType = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 17))
if mibBuilder.loadTexts: productCasingType.setStatus('current')
productCasing = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 17, 33))
if mibBuilder.loadTexts: productCasing.setStatus('current')
productMainboard = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 17, 33, 31))
if mibBuilder.loadTexts: productMainboard.setStatus('current')
productInterfaces = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 17, 33, 31, 36))
if mibBuilder.loadTexts: productInterfaces.setStatus('current')
productSubType = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 17, 33, 31, 36, 255))
if mibBuilder.loadTexts: productSubType.setStatus('current')
productGeneral = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 17, 33, 31, 36, 255, 1))
if mibBuilder.loadTexts: productGeneral.setStatus('current')
productType = MibScalar((1, 3, 6, 1, 4, 1, 16108, 1, 17, 33, 31, 36, 255, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productType.setStatus('current')
mibBuilder.exportSymbols("GARDEROS-PRODUCT-MIB", productGroups=productGroups, product=product, productCasingType=productCasingType, productSubType=productSubType, productMainboard=productMainboard, productInformationGroup=productInformationGroup, productType=productType, productCompliances=productCompliances, productConformance=productConformance, PYSNMP_MODULE_ID=product, productModuleCompliance=productModuleCompliance, productCasing=productCasing, productGeneral=productGeneral, productInterfaces=productInterfaces, productMIB=productMIB)
