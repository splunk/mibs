#
# PySNMP MIB module CLOUDGENIX-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cloudgenix/CLOUDGENIX-SMI
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:36 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
enterprises, Bits, NotificationType, iso, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, TimeTicks, Counter32, Integer32, Unsigned32, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Bits", "NotificationType", "iso", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "TimeTicks", "Counter32", "Integer32", "Unsigned32", "ObjectIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cloudgenix = ModuleIdentity((1, 3, 6, 1, 4, 1, 50114))
cloudgenix.setRevisions(('2017-06-19 18:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cloudgenix.setRevisionsDescriptions(('Inital Revision',))
if mibBuilder.loadTexts: cloudgenix.setLastUpdated('202202241935Z')
if mibBuilder.loadTexts: cloudgenix.setOrganization('Palo Alto Networks, Inc.')
if mibBuilder.loadTexts: cloudgenix.setContactInfo('Prisma SD-WAN Support\n\n         Palo Alto Networks\n         3000 Tannery Way\n         Santa Clara, CA 95054\n         USA\n\n         Technical Support\n         N. America: +1 408 738 7799\n         EMEA: +31 20 808 4600\n         APAC: +65 3158 5600\n\n         support@paloaltonetworks.com')
if mibBuilder.loadTexts: cloudgenix.setDescription('Structure of Management Information for Prisma SD-WAN')
class CgxDegreesC(TextualConvention, Integer32):
    description = 'Units are reported on the wire in milidegrees Celsius.\n         CgxDegreesC provides a textual-convention to display Degrees\n         Celsius (C).'
    status = 'current'
    displayHint = 'd-3'

class CgxVolts(TextualConvention, Integer32):
    description = 'Units are reported on the wire in milivolts. CgxVolts provides\n         a textual-convention to display as Volts (V).'
    status = 'current'
    displayHint = 'd-3'

cgxObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 50114, 1))
cgxConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 50114, 2))
cgxCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 50114, 2, 1))
cloudgenixCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 50114, 2, 1, 1)).setObjects()

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cloudgenixCompliance = cloudgenixCompliance.setStatus('current')
if mibBuilder.loadTexts: cloudgenixCompliance.setDescription('Compliance statement for entities which implement the Prisma\n         SD-WAN SMI MIB')
cgxGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 50114, 2, 2))
cgxMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 50114, 10))
if mibBuilder.loadTexts: cgxMgmt.setStatus('current')
if mibBuilder.loadTexts: cgxMgmt.setDescription('Root Object Identifier for Prisma SD-WAN Management-related\n         Objects')
cgxProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 50114, 11))
if mibBuilder.loadTexts: cgxProducts.setStatus('current')
if mibBuilder.loadTexts: cgxProducts.setDescription('Root Object Identifier for Prisma SD-WAN Product specific\n         Objects')
mibBuilder.exportSymbols("CLOUDGENIX-SMI", cgxConformance=cgxConformance, CgxVolts=CgxVolts, cloudgenix=cloudgenix, cgxObjects=cgxObjects, cgxCompliances=cgxCompliances, cgxMgmt=cgxMgmt, PYSNMP_MODULE_ID=cloudgenix, CgxDegreesC=CgxDegreesC, cgxProducts=cgxProducts, cloudgenixCompliance=cloudgenixCompliance, cgxGroups=cgxGroups)
