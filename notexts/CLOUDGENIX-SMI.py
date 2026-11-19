#
# PySNMP MIB module CLOUDGENIX-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cloudgenix/CLOUDGENIX-SMI
# Produced by pysmi-1.1.12 at Thu Nov 19 08:31:59 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, ObjectIdentity, Gauge32, MibIdentifier, NotificationType, IpAddress, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, Integer32, Unsigned32, TimeTicks, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "Gauge32", "MibIdentifier", "NotificationType", "IpAddress", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "Integer32", "Unsigned32", "TimeTicks", "Bits", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cloudgenix = ModuleIdentity((1, 3, 6, 1, 4, 1, 50114))
cloudgenix.setRevisions(('2017-06-19 18:00',))
if mibBuilder.loadTexts: cloudgenix.setLastUpdated('202202241935Z')
if mibBuilder.loadTexts: cloudgenix.setOrganization('Palo Alto Networks, Inc.')
class CgxDegreesC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-3'

class CgxVolts(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-3'

cgxObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 50114, 1))
cgxConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 50114, 2))
cgxCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 50114, 2, 1))
cloudgenixCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 50114, 2, 1, 1)).setObjects()

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cloudgenixCompliance = cloudgenixCompliance.setStatus('current')
cgxGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 50114, 2, 2))
cgxMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 50114, 10))
if mibBuilder.loadTexts: cgxMgmt.setStatus('current')
cgxProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 50114, 11))
if mibBuilder.loadTexts: cgxProducts.setStatus('current')
mibBuilder.exportSymbols("CLOUDGENIX-SMI", CgxDegreesC=CgxDegreesC, cloudgenixCompliance=cloudgenixCompliance, cloudgenix=cloudgenix, cgxProducts=cgxProducts, cgxObjects=cgxObjects, cgxGroups=cgxGroups, cgxConformance=cgxConformance, CgxVolts=CgxVolts, cgxMgmt=cgxMgmt, PYSNMP_MODULE_ID=cloudgenix, cgxCompliances=cgxCompliances)
